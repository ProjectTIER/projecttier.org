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
      url: `${global.chooserUrls.imageChooser}?select_format=true`,  // TODO: use custom ModalWorkflow
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

    // Uses the Draft.js API to create a new entity with the right data.
    const contentWithEntity = content.createEntity(entityType.type, 'IMMUTABLE', {
        tip: "TIP CONTENT GOES HERE", // TODO
    });
    const entityKey = contentWithEntity.getLastCreatedEntityKey();

    // We also add some text for the entity to be activated on.
    const text = 'ⓘ';

    const newContent = Modifier.replaceText(content, selection, text, null, entityKey);
    const nextState = EditorState.push(editorState, newContent, 'insert-characters');

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
