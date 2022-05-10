function addToFavorites() {
    document.getElementById('result').innerHTML = "";
    let checkboxes = document.getElementsByTagName("input");
    let favorites = [];

    for (let i = 0; i < checkboxes.length; i++)
    {
        if (checkboxes[i].type == "checkbox")
        {
            if (checkboxes[i].checked == true)
            {
                let stock = checkboxes[i].nextElementSibling.textContent;
                let stockname = stock.split(" - ")[0];

                if (!favorites.includes(stockname))
                    favorites.push(stockname);



            }
        }
    }
    for (const fav of favorites)
    {
        document.getElementById('result').innerHTML += "<br>" + fav + "<br>";
    }
}