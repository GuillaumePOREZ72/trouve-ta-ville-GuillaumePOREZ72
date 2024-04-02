import React, { useState } from 'react'

const Search = ({setSearch}) => {
  cosnt [input, setInput] = useState("");

  const handleChange= (event) => {
    setInput(event.target.value);
  }

const handleSubmit = (event) => {
  event.preventDefault();
  setSearch(input);
}
  return (
  <form onSubmit={handleSubmit}>
    <label htmlFor='search'>Nom de la commune</label>
    <input type="text" id='search' name='search' placeholder='Recherche...' value={input} onChange={handleChange} />
    <button type="submit">Chercher</button>
  </form>
  )
}

export default Search;