import React from "react";

const BookItem = ({book}) => {
    return(
        <tr>
            <td>{book.id}</td>
            <td>{book.name}</td>
            <td>{book.authors}</td>
        </tr>
    )
}

const BookList = ({books}) =>  {
    return(
        <table>
            <th>ID книги</th>
            <th>Название книги</th>
            <th>Авторы</th>
            {books.map((book_) => <BookItem book={book_}/>)}
        </table>
    )
}

export default BookList