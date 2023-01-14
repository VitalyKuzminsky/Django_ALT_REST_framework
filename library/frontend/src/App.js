import logo from './logo.svg';
import './App.css';
import React from "react";
import AuthorList from "./components/Author";
//import BookList from "./components/Book";
import axios from "axios";

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state={
            'authors': [],
//            'books':[]
        }
    }

    componentDidMount() {
//        const authors = [
//            {
//                'first_name':' Фёдор',
//                'last_name':' Достаевский',
//                'birthday_year': 1821,
//            },
//            {
//                'first_name': 'Александр',
//                'last_name':' Грин',
//                'birthday_year': 1880,
//            },
//        ]
        axios.get('http://127.0.0.1:8000/api/authors/').then(response => {
            const authors = response.data
            this.setState({
                'authors': authors
            })
        }).catch(error => console.log(error))
//        axios.get('http://127.0.0.1:8000/api/book/').then(response => {
//            const books = response.data
//            this.setState({
//                'books': books
//            })
//        }).catch(error => console.log(error))

//        this.setState({
//            'authors': authors
//        })

    }

    render() {
        return (
            <div>
                <div>
                    <AuthorList authors={this.state.authors}/>
                </div>
            </div>
        );
    }
}

export default App;
