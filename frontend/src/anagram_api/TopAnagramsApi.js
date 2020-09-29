import {APIError} from "./APIError";

export const getTopAnagramSubmissions = async () => {
    /**
     * Submits a list of words as potential anagrams and returns the server response.
     *
     * @param string words The words to submit to the anagram submission API
     * @return {object} The response from the server
     */
    let response = await fetch(`http://localhost:5000/anagram/top`, {
        method: "GET",
        mode: "cors"
    })

    if (!response.ok) {
        throw new APIError(await response.text(), "getTopAnagramSubmissions", response.status)
    }

    return response.json()
}
