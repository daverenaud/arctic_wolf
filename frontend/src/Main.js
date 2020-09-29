import React, {Component} from "react";
import {BrowserRouter, NavLink, Route} from "react-router-dom";
import Home from "./Home";
import AnagramSubmission from "./pages/AnagramSubmission";
import TopAnagrams from "./pages/TopAnagrams";
import Header from "./Header";
import './App.css'

export default class Main extends Component {
    onNavLinkClick(event) {
        event.target.parentElement.querySelector('.active').classList.remove('active')
        event.target.classList.add('active')
    }

    render() {
        return (
            <BrowserRouter>
                <div className="app">
                    <Header />
                    <div className="tab-bar">
                        <NavLink className="tab-bar-item" to="/" onClick={this.onNavLinkClick}>Home</NavLink>
                        <NavLink className="tab-bar-item" to="/anagram_submission" onClick={this.onNavLinkClick}>Submit Anagram</NavLink>
                        <NavLink className="tab-bar-item" to="/top_anagrams" onClick={this.onNavLinkClick}>Top Anagrams</NavLink>
                    </div>
                    <div className="content">
                        <Route exact path="/" component={Home}/>
                        <Route path="/anagram_submission" component={AnagramSubmission}/>
                        <Route path="/top_anagrams" component={TopAnagrams}/>
                    </div>
                </div>
            </BrowserRouter>
        )
    }
}
