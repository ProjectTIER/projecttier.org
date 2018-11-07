const React = window.React;
const Modifier = window.DraftJS.Modifier;
const EditorState = window.DraftJS.EditorState;

const DEMO_TIPS = ['AMD', 'AAPL', 'TWTR', 'TSLA', 'BTC'];

// Not a real React component – just creates the entities as soon as it is rendered.
class TipSource extends React.Component {
    componentDidMount() {
        const { editorState, entityType, onComplete } = this.props;

        const content = editorState.getCurrentContent();
        const selection = editorState.getSelection();

        const randomTip = DEMO_TIPS[Math.floor(Math.random() * DEMO_TIPS.length)];

        // Uses the Draft.js API to create a new entity with the right data.
        const contentWithEntity = content.createEntity(entityType.type, 'IMMUTABLE', {
            tip: randomTip,
        });
        const entityKey = contentWithEntity.getLastCreatedEntityKey();

        // We also add some text for the entity to be activated on.
        const text = `$${randomTip}`;

        const newContent = Modifier.replaceText(content, selection, text, null, entityKey);
        const nextState = EditorState.push(outlineeditorState, newContent, 'insert-characters');

        onComplete(nextState);
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
            window.open(`https://finance.yahoo.com/quote/${data.tip}`);
        },
    }, props.children);
};


window.draftail.registerPlugin({
    type: 'TIP',
    source: TipSource,
    decorator: Tip,
});


[].slice.call(document.querySelectorAll('[data-tip]')).forEach((elt) => {
    const link = document.createElement('a');
    link.href = `https://finance.yahoo.com/quote/${elt.dataset.tip}`;
    link.innerHTML = `${elt.innerHTML}<svg width="50" height="20" stroke-width="2" stroke="blue" fill="rgba(0, 0, 255, .2)"><path d="M4 14.19 L 4 14.19 L 13.2 14.21 L 22.4 13.77 L 31.59 13.99 L 40.8 13.46 L 50 11.68 L 59.19 11.35 L 68.39 10.68 L 77.6 7.11 L 86.8 7.85 L 96 4" fill="none"></path><path d="M4 14.19 L 4 14.19 L 13.2 14.21 L 22.4 13.77 L 31.59 13.99 L 40.8 13.46 L 50 11.68 L 59.19 11.35 L 68.39 10.68 L 77.6 7.11 L 86.8 7.85 L 96 4 V 20 L 4 20 Z" stroke="none"></path></svg>`;

    elt.innerHTML = '';
    elt.appendChild(link);
});
