import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
  signup = 0;
  showSignup(){
    this.signup=1;
  };
  showDestination(){
    this.signup=2;
  };
  showHome(){
    this.signup=0;
  };
}
