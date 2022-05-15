import axios from "axios";

export interface Token {
    word: string
    furigana: string
}

export default function tokenize(text: string) {
    return new Promise<Token[]>((resolve, reject) => {
        axios.post('/api/v1/tokenize', {'text': text})
            .then(resp => {
                console.log(resp.data)
                resolve(resp.data)
            })
            .catch(err => {
                console.error(err)
                reject(err)
            })
    })
};
