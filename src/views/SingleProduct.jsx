import React, {useState, useEffect} from 'react';
import { useParams } from 'react-router-dom';

const SingleProduct = ({addToCart}) => {
    const { id } = useParams()

    const [product, setProduct] = useState({})

    const getSingleProduct = async ()=>{
        const res = await fetch(`http://127.0.0.1:5000/api/shop/${id}`)
        const data = await res.json()
        setProduct(data)
    }

    useEffect(()=>{
        getSingleProduct()
    },[])

    return (
        <div className="container productSize mt-3">
            <div className="card text-decoration-none text-dark">
                <img src={product.image} className="card-img-top p-4" alt="..." />
                <div className="card-body">
                    <h5 className="card-title">{product.name}</h5>
                    <p className="card-text">{product.description}</p>
                    <h3>{product.price}</h3> <button onClick={() => addToCart(product)} className='btn btn-secondary'>Add To Cart</button>
                </div>
            </div>
        </div>
    )
};

export default SingleProduct;