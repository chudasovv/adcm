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
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';

import { AuthGuard } from '../../core/auth/auth.guard';
import { BundleListComponent, MainComponent, LicenseComponent } from './bundle-list.component';
import { SharedModule } from '@app/shared/shared.module';
import { BundleDetailsComponent } from '../../components/bundle/bundle-details/bundle-details.component';

const routes: Routes = [
  {
    path: '',
    canActivate: [AuthGuard],
    component: BundleListComponent,
  },
  {
    path: ':bundle',
    canActivate: [AuthGuard],
    component: BundleDetailsComponent,
    children: [
      { path: '', redirectTo: 'main', pathMatch: 'full' },
      { path: 'main', component: MainComponent },
      { path: 'license', component: LicenseComponent },
    ],
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class BundleRoutingModule {}

@NgModule({
  declarations: [BundleListComponent, MainComponent, LicenseComponent],
  imports: [CommonModule, SharedModule, BundleRoutingModule, RouterModule, BundleRoutingModule],
})
export class BundleModule {}
