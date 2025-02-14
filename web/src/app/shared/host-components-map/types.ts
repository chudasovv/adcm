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
import { IComponent, Host, IRequires } from '@app/core/types';

export type ActionParam = 'add' | 'remove';
export type TConstraintValue = number | '+' | 'odd' | 'depend';
export type TConstraint = TConstraintValue[];

export interface IRawHosComponent {
  component: IComponent[];
  host: Partial<Host>[];
  hc: Post[];
}

export interface Post {
  id?: number;
  host_id: number;
  service_id: number;
  component_id?: number;
}

export interface PrototypePost extends Post {
  component_prototype_id: number;
}

export class Post implements Post {
  constructor(public host_id: number, public service_id: number, public component_id?: number,  public id?: number ) {}
}

export class PrototypePost implements Post {
  constructor(public host_id: number, public service_id: number, public component_prototype_id: number, public id?: number ) {}
}

/**
 *```
  {
    id: number;
    name: string;
    relations: Tile[] = [];
    isSelected?: boolean;
    isLink?: boolean;
    limit?: Constraint;
    disabled: boolean;
    actions?: ActionParam[];
    color?: 'none' | 'white' | 'gray' | 'yellow';
    notification?: string;
  }
 ```
 * @class Tile
 */
export class Tile {
  id: number;
  name: string;
  relations: Tile[] = [];
  isSelected?: boolean;
  isLink?: boolean;
  limit?: TConstraint;
  disabled: boolean;
  actions?: ActionParam[];
  color?: 'none' | 'white' | 'gray' | 'yellow';
  notification?: string;
  mm?: string;
  is_prototype?: boolean;
}

export class HostTile extends Tile {
  constructor(rawHost: Partial<Host>) {
    super();
    this.id = rawHost.id;
    this.name = rawHost.fqdn;
    this.mm = rawHost.maintenance_mode;
  }
}

export class CompTile extends Tile {
  prototype_id: number;
  service_id: number;
  component: string;
  requires: IRequires[];
  constructor(rawComponent: IComponent, public actions?: ActionParam[]) {
    super();
    if (rawComponent) {
      this.id = rawComponent.id;
      this.service_id = rawComponent.service_id;
      this.component = `${rawComponent.service_name}/${rawComponent.name}`;
      this.name = rawComponent.display_name;
      this.disabled = rawComponent.service_state !== 'created';
      this.limit = rawComponent.constraint;
      this.requires = rawComponent.requires;
      this.prototype_id = rawComponent.prototype_id;
    }
    this.is_prototype = this.isPrototype(rawComponent);
  }

  isPrototype(component): boolean {
    return component?.url?.includes('prototype')
  }
}

/**
 * State user selection
 *
 * @class StatePost
 */
export class StatePost {
  private _data: Post[];

  constructor() {
    this._data = [];
  }

  private _compare(a: Post, b: Post) {
    return a.host_id === b.host_id && a.service_id === b.service_id && a.component_id === b.component_id;
  }

  get data() {
    return this._data;
  }

  add(post: Post) {
    const f = this._data.find((p) => this._compare(p, post));
    if (!f) this._data.push(post);
    else if (!f.id) f.id = post.id;
  }

  delete(post: Post) {
    this._data = this._data.filter((p) => !this._compare(p, post));
  }

  clear() {
    this._data = [];
  }

  update(data: Post[]) {
    data.forEach((a) => this.add(this.containsPrototype(a)));
  }

  containsPrototype(component): Post | PrototypePost {
   if (component?.url?.includes('prototype')) {
     return new PrototypePost(component.host_id, component.service_id, component.id);
   }

   return new Post(component.host_id, component.service_id, component.component_id, component.id);
  }
}
/**
 *```
  {
    link: Tile;
    linkSource: Tile[];
    selected: Tile;
  }
  *```
 */
export interface IStream {
  link: Tile;
  linkSource: Tile[];
  selected: Tile;
}
