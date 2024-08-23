// HomePage.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

function HomePage() {
  const [products, setProducts] = useState([]);
  const [filter, setFilter] = useState('');

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/categories/') // replace with your API URL
      .then(response => {
        setProducts(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the data!', error);
      });
  }, []);

  const filteredProducts = products.filter(product =>
    (product.title || '').toLowerCase().includes(filter.toLowerCase())
  );

  return (
    <div>
      <input
        type="text"
        placeholder="Search by title..."
        value={filter}
        onChange={(e) => setFilter(e.target.value)}
      />
      <div className="product-list">
        {filteredProducts.map(product => (
          <div key={product.id} className="product-item">
            <h3>{product.title}</h3>
            <p>{product.color}</p>
            <Link to={`/product/${product.id}`}>View Details</Link>
          </div>
        ))}
      </div>
    </div>
  );
}

export default HomePage;
