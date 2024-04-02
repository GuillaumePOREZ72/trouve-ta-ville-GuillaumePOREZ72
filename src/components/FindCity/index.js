import List from "../List";
import Search from "../Search";
import { useState } from "react";

const FindCity = () => {
  const [search,  setSearch] = useState("");
  const [citiesList,  setCitiesList] = useState([]);
  const [isLoading, setIsLoading]  = useState(false)

  const getCities = async () => {
    try {
      setIsLoading(true)
      const response = await fetch(`https://geo.api.gouv.fr/communes?nom=${search}`)
      const cities = await response.json();
      setCitiesList(cities);
      setIsLoading(false)
    } catch (error) {
      console.error(error.message);
      setIsLoading(false)
    }
  }

  useEffect(() => {
    getCities()
  }, [search])

  return (
    <section>
      <h1>Rechecrche par nom de commune</h1>
      <Search setSearch= {setSearch} />
      {!isLoading && <List citiesList={citiesList}/>}
      {isLoading && <h2>Chargement des données en cours...</h2>}
    </section>
  );
};

export default FindCity;
