import React, { Component } from 'react'
import { Link } from 'react-router-dom'
import '../css/styles.css'

export default class Navbar extends Component {

    render() {

        return (
            <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                <div className="container-fluid">
                    <Link className="navbar-brand nav-link" to="/">Arcade</Link>
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                            <li className="nav-item">
                                <Link className="nav-link active" aria-current="page" to="/">Home</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" to="/shop">Shop</Link>
                            </li>
                            {
                                this.props.isLoggedIn ? (
                                    <>
                                        <li className="nav-item">
                                            <Link className="nav-link" to="/chat">Social</Link>
                                        </li>
                                        <li className="nav-item align-end">
                                            <p className="m-2 text-light" to="/login">Hello, {this.props.currentUser.username}</p>
                                        </li>
                                        <li className="nav-item align-end">
                                            <button className="btn btn-danger btn-sm m-1" onClick={this.props.onLogOut}>Log Out</button>
                                        </li>
                                    </>
                                ) : (
                                    <>
                                        <li className="nav-item">
                                            <Link className="nav-link" to="/login">Log in</Link>
                                        </li>
                                        <li className="nav-item">
                                            <Link className="nav-link" to="/register">Sign Up</Link>
                                        </li>
                                    </>
                                )
                            }
                            <li className="nav-item">
                                <Link to='/cart' className='nav-link text-light'>{this.props.cart.length} | {this.props.sumTotalCart(this.props.cart)}</Link>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        )
    }
}