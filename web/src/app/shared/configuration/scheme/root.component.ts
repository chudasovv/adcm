// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
import { Component, OnInit, Input } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'app-root-scheme',
  template: `
    <div>
      <label>{{ options.name }} :: {{ options.type }}</label>
      <button mat-icon-button color="accent" (click)="add()">
        <mat-icon>add_circle_outline</mat-icon>
      </button>
    </div>
    <div class="content" [formGroup]="form">
      {{ form.value | json }}
    </div>
  `,
  styles: []
})
export class RootComponent implements OnInit {
  @Input() form = new FormGroup({});
  @Input() options: any;

  constructor() {}

  ngOnInit(): void {}

  add() {
    const rules = this.options.options[0];

    const itemFg = new FormGroup({});

    this.form.addControl(this.options.name, itemFg);

    rules.map(x => {
      itemFg.addControl(x.name, new FormControl());
    });
  }
}
