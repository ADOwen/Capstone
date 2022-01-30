import React, {useState, useEffect} from 'react';
import Post from '../components/Post';
import { Link } from 'react-router-dom';


const Blog = () => {

    const [posts, setPosts] = useState(()=>[])


    const getPosts = async () => {
        const res = await fetch('http://127.0.0.1:5000/api/posts')
        const data = await res.json()
        console.log(data)
        return data
}


    const loopThroughPosts = (listOfPosts) => {
        console.log(listOfPosts, 'did i run?')
      return listOfPosts.map(post => <Post key={post.id} post ={post}/> )
  } 
  
  useEffect(async ()=>{
      const data = await getPosts();
      setPosts(data)
      return 
    }, [])
  
  return (
      <div className="column">
          {loopThroughPosts(posts)}
          <Link to='/posts/create'><button className='btn btn-primary btn-sm mt-3'>Create post</button></Link>
      </div>
  )
};

export default Blog;
