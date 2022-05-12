import CryptoJS from 'crypto-js'
import axios from 'axios'

interface YoudaoRequest {
    q: string
    appKey: string
    salt: number
    from: string
    to: string
    sign: string
    signType: string
    curtime: number
}

const appKey = import.meta.env.VITE_YOUDAO_APPID
const key = import.meta.env.VITE_YOUDAO_SECRET

function truncate(input: string) {
    const len = input.length
    if (len <= 20) {
        return input
    }
    return input.substring(0, 10) + len + input.substring(len - 10, len)
}

export default async function translate(text: string) {
    const salt = (new Date).getTime()
    const curtime = Math.round(new Date().getTime() / 1000)

    const from = 'auto'
    const to = 'zh-CHS'

    const msg = appKey + truncate(text) + salt + curtime + key
    const sign = CryptoJS.SHA256(msg).toString(CryptoJS.enc.Hex)

    const payload: YoudaoRequest = {
        q: text,
        appKey: appKey,
        salt: salt,
        from: from,
        to: to,
        sign: sign,
        signType: 'v3',
        curtime: curtime,
    }
    const formData = new FormData()
    Object.entries(payload).forEach(([k, v]) => {
        formData.append(k, v);
    })

    const response = await axios.post('/api', formData)
    return response.data
}
