import React, {Component} from "react";
import {getTopAnagramSubmissions} from "../anagram_api/TopAnagramsApi";

export default class TopAnagrams extends Component {

    constructor(props) {
        super(props);
        this.state = {
            top_anagrams: []
        }
        this.refresh_top_anagram_submissions = this.refresh_top_anagram_submissions.bind(this)
    }

    async refresh_top_anagram_submissions() {
        let response = await getTopAnagramSubmissions()
        this.setState(() => {
            return {
                top_anagrams: response["top_anagrams"]
            }
        })
    }

    componentDidMount() {
        // No need to wait for the async function to finish. The component will re-render automatically.
        this.refresh_top_anagram_submissions()
    }

    render() {
        return <table className={"top_results_table"}>
            <thead>
            <tr>
                <th>Anagram</th>
                <th>Submission Count</th>
            </tr>
            </thead>
            <tbody>
            {this.state.top_anagrams.map((submission) => {
                return <tr>
                    <td>{submission["anagram"].join(", ")}</td>
                    <td>{submission["count"]}</td>
                </tr>
            })}
            </tbody>
        </table>
    }
}
