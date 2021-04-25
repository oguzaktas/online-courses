import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { UserSettings } from './user-settings';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(private http: HttpClient) { }

  public postUserSettingsForm(userSettings: UserSettings) : Observable<any> {
    return this.http.post('https://putsreq.com/fb2wSarnhve2sc7FzNga', userSettings);
    // return of(userSettings);
  }

  public getSubscriptionTypes(): Observable<string[]> {
    return of(['Monthly', 'Annual', 'Lifetime']);
  }
}
