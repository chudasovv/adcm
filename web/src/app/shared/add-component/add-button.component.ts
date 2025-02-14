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
import { Component, EventEmitter, Inject, Input, OnDestroy, Output, Type } from '@angular/core';
import { MatDialog, MatDialogConfig } from '@angular/material/dialog';

import { DialogComponent } from '@app/shared/components';
import { BaseDirective } from '@app/shared/directives';
import { AddFormComponent } from './add-form.component';
import { ADD_SERVICE_PROVIDER, FormModel, IAddService } from '@app/shared/add-component/add-service-model';
import { BaseFormDirective } from '@app/shared/add-component/base-form.directive';

export type AddButtonDialogConfig = Pick<MatDialogConfig, 'width' | 'maxWidth' | 'position'>;

const ADCM_DEFAULT_ADD_DIALOG_CONFIG: AddButtonDialogConfig = {
  width: '75%',
  maxWidth: '1400px',
  position: {
    top: '50px'
  }
};

@Component({
  selector: 'app-add-button',
  template: `
    <ng-container *ngIf="!asIcon; else icon">
      <button [appForTest]="'create-btn'" mat-raised-button color="accent" (click)="showForm()">
        <mat-icon>library_add</mat-icon>&nbsp;<ng-content></ng-content>
      </button>
    </ng-container>
    <ng-template #icon>
      <button [appForTest]="'create-btn'" mat-icon-button color="primary" (click)="showForm()">
        <mat-icon>add</mat-icon>
      </button>
    </ng-template>
  `,
  styles: ['button {margin-right: 6px;}'],
})
export class AddButtonComponent extends BaseDirective implements OnDestroy {
  @Input() asIcon = false;
  @Input() name: string;
  @Input() component: Type<BaseFormDirective>;
  @Input() dialogConfig: AddButtonDialogConfig = {};
  @Input() clusterId: number;
  @Output() added = new EventEmitter();

  constructor(@Inject(ADD_SERVICE_PROVIDER) private service: IAddService,
              private dialog: MatDialog) {
    super();
  }

  showForm(data?: FormModel): void {

    const model: any = data || this.service?.model(this.name) || this.service.Cluster;
    if (this.component) {
      model.component = this.component;
    }

    if (this.clusterId) {
      model.clusterId = this.clusterId;
    }

    const name = model.title || model.name;
    let title;

    if (data) {
      title = `Update ${name}`;
    } else {
      title = `${['cluster', 'provider', 'host'].includes(name) ? 'Create' : 'Add'} ${name}`;
    }


    this.dialog.open(DialogComponent, {
      ...ADCM_DEFAULT_ADD_DIALOG_CONFIG,
      ...this.dialogConfig,
      data: {
        title,
        component: AddFormComponent,
        model,
      },
    });
  }
}
