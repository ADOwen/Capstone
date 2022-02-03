import React, { Component } from 'react';
import Phaser from 'phaser';

export default class App extends Component {
  constructor() {
    super();
    this.game=null
  }

  preload(){
    this.load.image('sky', 'assets/sky.png');
    this.load.image('ground', 'assets/platform.png');
    this.load.image('star', '../assets/star.png');
    this.load.image('bomb', 'assets/bomb.png');
    this.load.spritesheet('dude', 
        'assets/dude.png',
        { frameWidth: 32, frameHeight: 48 })
    this.load.spritesheet('player', 
        '../assets/adventurer.png',
        { frameWidth: 55, frameHeight: 37 })
  }

  create() {
    this.game.stage.backgroundColor = '#ffffff';
    this.add.image(400, 300, 'sky');
    this.add.image(400, 300, 'star');
  }
  
  update(){

  }
  

  componentDidMount() {
    this.game = new Phaser.Game(800, 600, Phaser.CANVAS, 'phaser-target',
      {
        preload: this.preload.bind(this),
        create: this.create.bind(this),
        update: this.update.bind(this)
      }
    );

    console.log(this.game);
  }



  render() {
    return (
      <section id="phaser-target">
        hello there old friend
      </section>
    )
  }
}
