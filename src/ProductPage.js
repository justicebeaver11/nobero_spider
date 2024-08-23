// ProductPage.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

function ProductPage() {
  const { id } = useParams();
  const [product, setProduct] = useState(null);

  useEffect(() => {
    axios.get(`http://127.0.0.1:8000/api/products/${id}/`) // replace with your API URL
      .then(response => {
        setProduct(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the product data!', error);
      });
  }, [id]);

  if (!product) return <div>Loading...</div>;

  return (
    <div>
      <h1>{product.title}</h1>
      <p>Color: {product.color}</p>
      {/* Add other product details here */}
    </div>
  );
}

export default ProductPage;
