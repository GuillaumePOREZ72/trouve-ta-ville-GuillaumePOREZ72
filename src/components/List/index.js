import React from "react";
import Item from "./Item.js";

const List = ({citiesList}) => {
  return (
    <section>
      <div>
        <h2>Résultats</h2>
        <button>Changer le format</button>
      </div>
      <ul>
       {citiesList.map(city => <Item key={city.code} codesPostaux={city.codesPostaux} population={city.population} nom={city.nom} codeDepartement={city.codeDepartement}></Item> )}
      </ul>
    </section>
  );
};

export default List;
