import axios from "axios";

export default function translate(text: string) {
    return new Promise<string>((resolve, reject) => {
        axios.post('/api/v1/translate', {'text': text})
            .then(resp => {
                if (resp.data && resp.data['code'] == '0') {
                    resolve(resp.data['translation'].join(''))
                } else {
                    reject({'code': resp.data['code']})
                }
            })
            .catch(err => {
                console.error(err)
                reject(err)
            })
    });
};