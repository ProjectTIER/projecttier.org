const React = window.React;
const Modifier = window.DraftJS.Modifier;
const EditorState = window.DraftJS.EditorState;


// Not a real React component – just creates the entities as soon as it is rendered.
class TipSource extends React.Component {
    componentDidMount() {
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

        var modal = ModalWorkflow({
            url: window.chooserUrls.documentChooser,
            onload: DOCUMENT_CHOOSER_MODAL_ONLOAD_HANDLERS,
            responses: {
                documentChosen: function(docData) {
                    console.log("tip modal: document was selected")
                    modal.close();
                    onComplete(nextState);
                }
            }
        });

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
