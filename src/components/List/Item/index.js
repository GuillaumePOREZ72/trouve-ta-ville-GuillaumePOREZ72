import React from 'react'

const Item = ({nom, codesPostaux, codeDepartement, population}) => {
  return (
   
      <li>
<span>{nom} - {codeDepartement}</span>
<span>Code postal: {codesPostaux}</span>
<span>Population: {population}</span>
      </li>
  )
}

export default Item;