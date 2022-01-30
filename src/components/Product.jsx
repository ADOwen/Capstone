import React from 'react';
import { Link } from 'react-router-dom';
import '../css/product.css'


const Product = ({product, addToCart , addToCartAPI, user_id}) => {
    const p = product
    
    
    return (
        <>
        <h1>Shop Page</h1>
        <div className="container product-size mt-3">
            <div className="card text-decoration-none text-dark">
                <Link  to={`/shop/${p.id}`}>
                    <img src={ p.image } className="card-img-top p-4" alt="..."/>
                </Link>
                    <div className="card-body">
                        <h5 className="card-title">{ p.name }</h5>
                        <p className="card-text">{ p.description }</p>
                        <h3>{ p.price }</h3> <button onClick={()=>{ addToCartAPI(user_id,p.id); addToCart(p)}} className='btn btn-secondary'>Add To Cart</button>
                    </div>
            </div>
        </div>
        </>
    )
};

export default Product;
