import {APIError} from "./APIError";

export const submitAnagram = async (...words) => {
    /**
     * Submits a list of words as potential anagrams and returns the server response.
     *
     * @param string words The words to submit to the anagram submission API
     * @return {object} The response from the server
     */
    let response = await fetch(`http://localhost:5000/anagram`, {
        method: "POST",
        mode: "cors",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            "words": words
        })
    })

    if (!response.ok) {
        throw new APIError(await response.text(), "submitAnagram", response.status)
    }

    return response.json()
}
