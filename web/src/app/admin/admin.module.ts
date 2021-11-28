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
import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { SharedModule } from '@app/shared/shared.module';
import { AuthGuard } from '@app/core/auth/auth.guard';
import { IntroComponent } from './intro.component';
import { PatternComponent } from './pattern.component';
import { SettingsComponent } from './settings.component';
import { UsersComponent } from './users/users.component';
import { AdwpFormElementModule } from '../../../../../adwp_ui/projects/widgets/src/lib/form-element/form-element.module';
import { RbacGroupModule } from '../components/rbac/group/rbac-group.module';
import { RbacUserModule } from '../components/rbac/user/rbac-user.module';
import { RbacRoleModule } from '../components/rbac/role/rbac-role.module';

import { GroupsComponent } from './groups/groups.component';
import { RolesComponent } from './roles/roles.component';
import { PoliciesComponent } from './policies/policies.component';

const routes: Routes = [
  {
    path: '',
    component: PatternComponent,
    canActivate: [AuthGuard],
    canActivateChild: [AuthGuard],
    children: [
      {
        path: '',
        redirectTo: 'intro',
        pathMatch: 'full',
      },
      {
        path: 'intro',
        component: IntroComponent,
      },
      {
        path: 'settings',
        component: SettingsComponent,
      },
      {
        path: 'users',
        component: UsersComponent,
      },
      {
        path: 'groups',
        component: GroupsComponent,
      },
      {
        path: 'roles',
        component: RolesComponent,
      },
      {
        path: 'policies',
        component: PoliciesComponent,
      }
    ],
  },
];

@NgModule({
  imports: [
    CommonModule,
    RouterModule.forChild(routes),
    SharedModule,
    AdwpFormElementModule, RbacUserModule, RbacGroupModule, RbacUserModule, RbacRoleModule
  ],
  declarations: [
    IntroComponent,
    SettingsComponent,
    UsersComponent,
    PatternComponent,
    GroupsComponent,
    RolesComponent,
    PoliciesComponent,
  ],
})
export class AdminModule {}
