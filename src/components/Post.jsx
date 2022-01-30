import React from 'react';
import { Link } from 'react-router-dom';
import '../css/post.css'

export const Post = ({post}) => {

  return (
      <div className='container post-container'>
          <Link className ="card text-decoration-none text-dark" to="">
              <div className="card-header">
                  <p>{post.id}</p>
              </div>
            <div className="card-body">
                <p className="card-text">{post.text}</p>
            </div>
            <div className="card-footer">today</div>
          </Link>
      </div>
  )
};

export default Post;