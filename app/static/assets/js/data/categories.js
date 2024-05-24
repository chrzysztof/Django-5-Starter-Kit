var url = '/items/api/categories/';
fetch(url)
  .then(response => response.json())
  .then(data => {
    window.categories = data.map(item => ({
        id: item.id,
        name: item.name,
        description: item.description
    }));
    console.log('Dane kategorii zostały pobrane:', window.categories);
  })
  .catch(error => {
    console.error('Wystąpił błąd podczas pobierania danych kategorii:', error);
  });