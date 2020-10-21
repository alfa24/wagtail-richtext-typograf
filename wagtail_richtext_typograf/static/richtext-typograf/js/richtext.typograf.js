const React = window.React;
const Modifier = window.DraftJS.Modifier;
const EditorState = window.DraftJS.EditorState;

class TypografSource extends React.Component {
    componentDidMount() {
        let nextState;
        const tp = new Typograf({locale: ['ru', 'en-US'],});

        const {editorState, entityType, onComplete} = this.props;
        const content = editorState.getCurrentContent();

        const selection = editorState.getSelection();
        const start = selection.getStartOffset();
        const end = selection.getEndOffset();

        if ((end - start) > 0) { // selected text
            const key = selection.getAnchorKey();
            const prev_text = content.getBlockForKey(key).text.slice(start, end);
            const next_text = tp.execute(prev_text);
            const newContent = Modifier.replaceText(content, selection, next_text)
            nextState = EditorState.push(editorState, newContent, 'insert-characters');
        } else { // all text
            let raw = window.DraftJS.convertToRaw(content)
            for (let i = 0; i < raw['blocks'].length; i++) {
                let prev_text = raw['blocks'][i].text;
                raw['blocks'][i].text = tp.execute(prev_text);
            }
            const newContent = window.DraftJS.convertFromRaw(raw);
            nextState = EditorState.push(editorState, newContent, 'change-block-data');
        }

        onComplete(nextState);
    }

    render() {
        return null;
    }
}


window.draftail.registerPlugin({
    type: 'TYPOGRAF',
    source: TypografSource,
});

