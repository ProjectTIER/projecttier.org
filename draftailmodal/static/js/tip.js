// Modal plugin for Draftail.
//
// Extending the Draftail Editor:
// https://docs.wagtail.io/en/latest/advanced_topics/customisation/extending_draftail.html

const React = window.React;
const Modifier = window.DraftJS.Modifier;
const EditorState = window.DraftJS.EditorState;


// When the ModalWorkflow endpoint responds, it'll tell us which one of
// these functions to run (by key name). Undocumented Wagtail stuff.
// See views.py for the endpoint code.
const TIP_MODAL_ONLOAD_HANDLERS = {
  "chooser": function(modal, jsonData) {
    $('form.draftailmodal').on('submit', function() {
      modal.postForm(this.action, $(this).serialize());
      return false;
    });
  },
  "tip_chosen": function(modal, jsonData) {
    modal.respond('tipChosen', jsonData); // ultimately passed to onChosen(data)
    modal.close();
  }
}


// Two Wagtail util functions useful for Drafttail.
// From here: https://github.com/wagtail/wagtail/blob/master/client/src/components/Draftail/DraftUtils.js
// FIXME: Figure out a way to import them instead of copying?
const getSelectedBlocksList = (editorState) => {
  const selectionState = editorState.getSelection();
  const content = editorState.getCurrentContent();
  const startKey = selectionState.getStartKey();
  const endKey = selectionState.getEndKey();
  const blockMap = content.getBlockMap();
  const blocks =  blockMap
    .toSeq()
    .skipUntil((_, k) => k === startKey)
    .takeUntil((_, k) => k === endKey)
    .concat([[endKey, blockMap.get(endKey)]]);
  return blocks.toList();
};
const getSelectionText = (editorState) => {
  const selection = editorState.getSelection();
  let start = selection.getAnchorOffset();
  let end = selection.getFocusOffset();
  const selectedBlocks = getSelectedBlocksList(editorState);
  if (selection.getIsBackward()) {
    const temp = start;
    start = end;
    end = temp;
  }
  let selectedText = '';
  for (let i = 0; i < selectedBlocks.size; i += 1) {
    const blockStart = i === 0 ? start : 0;
    const blockEnd = i === (selectedBlocks.size - 1) ? end : selectedBlocks.get(i).getText().length;
    selectedText += selectedBlocks.get(i).getText().slice(blockStart, blockEnd);
  }
  return selectedText;
};


// Returns the settings object for ModalWorkflow called in TipSource.
// This does not really need to be a separate function, but I'm too afraid
// to refactor it now.
function getChooserConfig(entityType, entity, selectedText) {
  if (entityType.type == 'TIP') {
    return {
      url: "/admin/draftailmodal/chooser/",  // FIXME: don't hardcode this?
      urlParams: undefined,
      onload: TIP_MODAL_ONLOAD_HANDLERS,
    };
  }
}


// The main plugin logic is here.
// This is a React component because of reasons I don't understand.
// It doesn't render anything, it's just a dummy that runs our code.
// Based off ModalWorkflowSource: https://github.com/wagtail/wagtail/blob/master/client/src/components/Draftail/sources/ModalWorkflowSource.js#L133
class TipSource extends React.Component {

  // Called when an instance is created
  constructor(props) {
    super(props);
    // set the value of `this`
    this.onChosen = this.onChosen.bind(this);
    this.onClose = this.onClose.bind(this);
  }

  // This gets run whenever the toolbar button for this plugin is clicked.
  // It's also run whenever props.onEdit() is called.
  componentDidMount() {
    const { onClose, entityType, entity, editorState, entityKey } = this.props;
    const selectedText = getSelectionText(editorState); // that utils function
    const { url, onload } = getChooserConfig(entityType, entity, selectedText); // that "settings object" function
    const contentState = editorState.getCurrentContent();
    var urlParams = {};

    // Try to edit an existing entity (if onEdit() was called)
    try {
      const data = contentState.getEntity(entityKey).getData();
      urlParams = {
        data: JSON.stringify(data['tip']),
        entityKey: entityKey
      };
    } catch(err) {}

    $(document.body).on('hidden.bs.modal', this.onClose); // FIXME: idk

    // Spawn the ModalWorkflow window where the text content is set!
    this.workflow = global.ModalWorkflow({
      url,
      urlParams,
      onload,
      responses: {
        tipChosen: this.onChosen, // calls the function below
      },
      onError: () => {
        console.log("modalworkflow error");
        onClose();
      },
    });
  }

  // FIXME: idk when this is called or what exactly it does
  componentWillUnmount() {
    this.workflow = null;
    $(document.body).off('hidden.bs.modal', this.onClose);
  }

  // Called when tip content has been entered and saved
  onChosen(data) {
    const tip_data = data['result'];
    const { editorState, entityType, onComplete } = this.props;
    const content = editorState.getCurrentContent();
    const selection = editorState.getSelection();

    // Update an entity (if it exists). Happens when an entity is clicked.
    if (data.entityKey) {
      const newContent = content.replaceEntityData(data.entityKey, {tip: tip_data});
      const nextState = EditorState.push(editorState, newContent, 'insert-characters');
      this.workflow.close();
      onComplete(nextState);
      return; // stop here
    }

    // Uses the Draft.js API to create a new entity with the right data.
    const contentWithEntity = content.createEntity(entityType.type, 'IMMUTABLE', {
        tip: tip_data,
    });
    const entityKey = contentWithEntity.getLastCreatedEntityKey();

    // We also add some text for the entity to be activated on.
    const text = 'tip';

    // FIXME: idk how this works
    const newContent = Modifier.replaceText(content, selection, text, null, entityKey);
    const nextState = EditorState.push(editorState, newContent, 'insert-characters');

    this.workflow.close(); // Needed for IE11, apparently

    onComplete(nextState); // FIXME: idk how this works
  }

  // FIXME: idk how this works
  onClose(e) {
    const { onClose } = this.props;
    e.preventDefault();
    onClose();
  }

  // Render nothing!
  render() {
    return null;
  }
}

// This is a Draft.js Decorator Component
// https://draftjs.org/docs/advanced-topics-decorators#decorator-components
// It creates the little "tip" icon rendered in the editor.
const Tip = (props) => {
    const { entityKey, contentState } = props;
    const data = contentState.getEntity(entityKey).getData();

    return React.createElement('a', {
        role: 'button',
        className: 'Draftail-inline--TIP',
        onMouseUp: () => {
            // When a tip is clicked, edit it.
            props.onEdit(entityKey);
        },
    }, props.children);
};

// Registers the plugin
// FIXME: I don't know this works
window.draftail.registerPlugin({
    type: 'TIP',
    source: TipSource,
    decorator: Tip,
});
