import logo from './logo.svg';
import './App.css';
import React from "react";
import AuthorList from "./components/Author";
import BookList from "./components/Book";
import NotFound404 from "./components/NotFound404";
import BooksAuthor from "./components/BooksAuthor";
import axios from "axios";
import {BrowserRouter, Route, Routes, Link, Navigate, HashRouter} from "react-router-dom";

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state={
            'authors': [],
            'books':[]
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
        axios.get('http://127.0.0.1:8000/api/books/').then(response => {
            const books = response.data
            this.setState({
                'books': books
            })
        }).catch(error => console.log(error))

//        this.setState({
//            'authors': authors
//        })

    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                        <div>
                            Меню:
                        </div>
                        <li>
                            <Link to='/'>
                                Авторы
                            </Link>
                        </li>
                        <li>
                            <Link to='/books'>
                                Книги
                            </Link>
                        </li>
                    </nav>

                    <Routes>
                        <Route exact path ='/' element={<Navigate to = '/authors'/>} />
                        <Route path ='/authors'>
                            <Route index element={<AuthorList authors={this.state.authors}/>} />
                            <Route path =':authorId' element={<BooksAuthor books={this.state.books}/>} />
                        </Route>


                        <Route exact path ='/books' element={<BookList books={this.state.books}/>} />
                        <Route path ='*' element={<NotFound404/>} />
                    </Routes>
                </BrowserRouter>
            </div>
        );
    }
}

export default App;
