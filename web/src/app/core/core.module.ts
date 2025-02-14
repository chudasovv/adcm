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
import { HTTP_INTERCEPTORS, HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';

import { ApiService } from '@app/core/api';
import { AuthGuard } from './auth/auth.guard';
import { AuthService } from './auth/auth.service';
import { RequestCacheService, RequestCache } from '@app/core/http-interseptors/request-cache.service';
import { CachingInterseptor } from '@app/core/http-interseptors/caching-interseptor';
import { AuthInterceptor } from '@app/core/http-interseptors/auth-interseptor';

@NgModule({
  imports: [HttpClientModule],
  providers: [
    ApiService,
    { provide: RequestCache, useClass: RequestCacheService },
    { provide: HTTP_INTERCEPTORS, useClass: CachingInterseptor, multi: true },
    { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true },
    AuthGuard,
    AuthService
  ],
})
export class CoreModule {}
