import React, {Component} from "react";
import {submitAnagram} from "../anagram_api/AnagramSubmissionApi";

export default class AnagramSubmission extends Component {
    constructor(props) {
        super(props);
        this.state = {
            submitted_anagrams: []
        }

        this.onSubmit = this.onSubmit.bind(this)
    }

    async onSubmit(event) {
        event.preventDefault()
        console.log(event)
        console.log(event.target)
        console.log(event.target.querySelectorAll(".word_input"))
        let words = Array.from(event.target.querySelectorAll(".word_input")).map((word_input) => {
            return word_input.value
        })
        try {
            let result = await submitAnagram(...words)
            this.setState((prevState) => {
                return {
                    submitted_anagrams: [
                        ...prevState.submitted_anagrams,
                        {
                            submitted_words: [...words],
                            is_anagram: result['words_are_anagrams']
                        }
                    ]
                }
            })
        } catch (e) {
            console.log(e)
        }
    }

    render() {
        return <div className={"content"}>
            <form onSubmit={this.onSubmit}>
                Word1<input type={"text"} className={"word_input"}/><br/>
                Word2<input type={"text"} className={"word_input"}/><br/>
                <input type={"submit"} value={"Submit Anagram"} title={"Submit"}/>
            </form>
            {this.state.submitted_anagrams.length > 0 && <div className={"submissions_view"}>
                <h2>Your Submissions</h2>
                <hr />
                <table className={"submissions_table"}>
                    <thead>
                    <tr>
                        <th>Words</th>
                        <th>Is an Anagram?</th>
                    </tr>
                    </thead>
                    <tbody>
                    {this.state.submitted_anagrams.reverse().map((submission) => {
                        return <tr>
                            <td>{submission["submitted_words"].join(", ")}</td>
                            <td>{submission["is_anagram"] ? "True" : "False"}</td>
                        </tr>
                    })}
                    </tbody>
                </table>
            </div>}
        </div>
    }
}
