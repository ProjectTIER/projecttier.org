const React = window.React;
const Modifier = window.DraftJS.Modifier;
const EditorState = window.DraftJS.EditorState;


/**
* Returns collection of currently selected blocks.
* See https://github.com/jpuri/draftjs-utils/blob/e81c0ae19c3b0fdef7e0c1b70d924398956be126/js/block.js#L19.
*/
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

/**
* Returns the currently selected text in the editor.
* See https://github.com/jpuri/draftjs-utils/blob/e81c0ae19c3b0fdef7e0c1b70d924398956be126/js/block.js#L106.
*/
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


function getChooserConfig(entityType, entity, selectedText) {
  if (entityType.type == 'TIP') {
    console.log("getChooserConfig: entityType.type == 'TIP'")
    return {
      url: `${global.chooserUrls.imageChooser}?select_format=true`,
      urlParams: {},
      onload: global.IMAGE_CHOOSER_MODAL_ONLOAD_HANDLERS,
    };
  }
}


class TipSource extends React.Component {
  constructor(props) {
    super(props);

    this.onChosen = this.onChosen.bind(this);
    this.onClose = this.onClose.bind(this);
  }

  componentDidMount() {
    const { onClose, entityType, entity, editorState } = this.props;
    const selectedText = getSelectionText(editorState);
    const { url, urlParams, onload } = getChooserConfig(entityType, entity, selectedText);

    $(document.body).on('hidden.bs.modal', this.onClose);

    // eslint-disable-next-line new-cap
    this.workflow = global.ModalWorkflow({
      url,
      urlParams,
      onload,
      responses: {
        imageChosen: this.onChosen,
        // Discard the first parameter (HTML) to only transmit the data.
        embedChosen: (_, data) => this.onChosen(data),
        documentChosen: this.onChosen,
        pageChosen: this.onChosen,
      },
      onError: () => {
        // eslint-disable-next-line no-alert
        window.alert(STRINGS.SERVER_ERROR);
        onClose();
      },
    });
  }

  componentWillUnmount() {
    this.workflow = null;

    $(document.body).off('hidden.bs.modal', this.onClose);
  }

  onChosen(data) {
    const { editorState, entityType, onComplete } = this.props;
    const content = editorState.getCurrentContent();
    const selection = editorState.getSelection();

    const entityData = filterEntityData(entityType, data);
    const mutability = MUTABILITY[entityType.type];
    const contentWithEntity = content.createEntity(entityType.type, mutability, entityData);
    const entityKey = contentWithEntity.getLastCreatedEntityKey();

    let nextState;

    if (entityType.block) {
      // Only supports adding entities at the moment, not editing existing ones.
      // See https://github.com/springload/draftail/blob/cdc8988fe2e3ac32374317f535a5338ab97e8637/examples/sources/ImageSource.js#L44-L62.
      // See https://github.com/springload/draftail/blob/cdc8988fe2e3ac32374317f535a5338ab97e8637/examples/sources/EmbedSource.js#L64-L91
      nextState = AtomicBlockUtils.insertAtomicBlock(editorState, entityKey, ' ');
    } else {
      // Replace text if the chooser demands it, or if there is no selected text in the first place.
      const shouldReplaceText = data.prefer_this_title_as_link_text || selection.isCollapsed();

      if (shouldReplaceText) {
        // If there is a title attribute, use it. Otherwise we inject the URL.
        const newText = data.title || data.url;
        const newContent = Modifier.replaceText(content, selection, newText, null, entityKey);
        nextState = EditorState.push(editorState, newContent, 'insert-characters');
      } else {
        nextState = RichUtils.toggleLink(editorState, selection, entityKey);
      }
    }

    // IE11 crashes when rendering the new entity in contenteditable if the modal is still open.
    // Other browsers do not mind. This is probably a focus management problem.
    // From the user's perspective, this is all happening too fast to notice either way.
    this.workflow.close();

    onComplete(nextState);
  }

  onClose(e) {
    const { onClose } = this.props;
    e.preventDefault();

    onClose();
  }

  render() {
    return null;
  }
}


// // Not a real React component – just creates the entities as soon as it is rendered.
// class TipSource extends React.Component {
//     componentDidMount() {
//         const { editorState, entityType, onComplete } = this.props;
//
//         const content = editorState.getCurrentContent();
//         const selection = editorState.getSelection();
//
//         // Uses the Draft.js API to create a new entity with the right data.
//         const contentWithEntity = content.createEntity(entityType.type, 'IMMUTABLE', {
//             tip: "TIP CONTENT GOES HERE", // TODO
//         });
//         const entityKey = contentWithEntity.getLastCreatedEntityKey();
//
//         // We also add some text for the entity to be activated on.
//         const text = 'ⓘ';
//
//         const newContent = Modifier.replaceText(content, selection, text, null, entityKey);
//         const nextState = EditorState.push(editorState, newContent, 'insert-characters');
//
//         var modal = ModalWorkflow({
//             url: window.chooserUrls.documentChooser,
//             onload: DOCUMENT_CHOOSER_MODAL_ONLOAD_HANDLERS,
//             responses: {
//                 documentChosen: function(docData) {
//                     console.log("tip modal: document was selected")
//                     modal.close();
//                     onComplete(nextState);
//                 }
//             }
//         });
//
//     }
//
//     render() {
//         return null;
//     }
// }

const Tip = (props) => {
    const { entityKey, contentState } = props;
    const data = contentState.getEntity(entityKey).getData();

    return React.createElement('a', {
        role: 'button',
        onMouseUp: () => {
            console.log("tip modal: info icon clicked");
        },
    }, props.children);
};

window.draftail.registerPlugin({
    type: 'TIP',
    source: TipSource,
    decorator: Tip,
});
