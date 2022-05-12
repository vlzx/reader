import kuromoji, {IpadicFeatures, Tokenizer} from 'kuromoji'

let tokenizer: Nullable<Tokenizer<IpadicFeatures>> = null

kuromoji.builder({}).build((err, _tokenizer) => {
    tokenizer = _tokenizer
})

export default function tokenize(text: string) {
    if (text == '' || tokenizer == null) {
        return []
    }
    try {
        return tokenizer.tokenize(text)
    } catch (e) {
        console.log(e)
        return []
    }
}
