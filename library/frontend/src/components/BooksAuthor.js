import React from "react";
import useParams from "react";

const BookItem = ({book}) => {
    return(
        <tr>
            <td>{book.id}</td>
            <td>{book.name}</td>
            <td>{book.authors}</td>
        </tr>
    )
}

const BooksAuthor = ({books}) =>  {
    let {authorId} = useParams()
    console.log(authorId)
//    let filter_books = books.filter((book) => book.authors.includes(authorId))
    let filter_books = books.filter((book) => book.authors.includes(String(authorId)))
//    let filter_books = books.filter((book) => book.authors.includes(authorName))
    return(
        <table>
            <th>ID книги</th>
            <th>Название книги</th>
            <th>Авторы</th>
            {filter_books.map((book_) => <BookItem book={book_}/>)}
        </table>
    )
}

export default BooksAuthor
//const BookItem = ({book}) => {
//    return(
//        <tr>
//            <td>{book.id}</td>
//            <td>{book.name}</td>
//            <td>{book.authors}</td>
//        </tr>
//    )
//}