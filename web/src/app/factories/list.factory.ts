import { IComponentColumn, IValueColumn, IButtonsColumn, ILinkColumn } from '@adwp-ui/widgets';
import { ComponentRef } from '@angular/core';

import { StateColumnComponent } from '@app/components/columns/state-column/state-column.component';
import { StatusColumnComponent, StatusData } from '@app/components/columns/status-column/status-column.component';
import { AdwpListDirective } from '@app/abstract-directives/adwp-list.directive';
import { UpgradeComponent } from '@app/shared/components';
import { ActionsButtonComponent } from '@app/components/actions-button/actions-button.component';
import { BaseEntity } from '@app/core/types';
import { ConcernListDirective } from '@app/abstract-directives/concern-list.directive';
import {
  MaintenanceModeButtonComponent
} from "@app/components/maintenance-mode-button/maintenance-mode-button.component";

export class ListFactory {

  static nameColumn(sort: string = 'name'): IValueColumn<any> {
    return {
      label: 'Name',
      sort,
      value: (row) => row.display_name || row.name,
    };
  }

  static fqdnColumn(): IValueColumn<any> {
    return {
      label: 'FQDN',
      sort: 'fqdn',
      className: 'width30pr',
      headerClassName: 'width30pr',
      value: row => row.fqdn,
    };
  }

  static descriptionColumn(): IValueColumn<any> {
    return {
      label: 'Description',
      value: (row) => row.description,
    };
  }

  static stateColumn(): IComponentColumn<any> {
    return {
      label: 'State',
      sort: 'state',
      type: 'component',
      className: 'width100',
      headerClassName: 'width100',
      component: StateColumnComponent,
    };
  }

  static statusColumn<T>(listDirective: AdwpListDirective<T>): IComponentColumn<T> {
    return {
      label: 'Status',
      sort: 'status',
      type: 'component',
      className: 'list-control',
      headerClassName: 'list-control',
      component: StatusColumnComponent,
      instanceTaken: (componentRef: ComponentRef<StatusColumnComponent<T>>) => {
        componentRef.instance.onClick
          .pipe(listDirective.takeUntil())
          .subscribe((data: StatusData<any>) => listDirective.gotoStatus(data));
      }
    };
  }

  static actionsButton<T extends BaseEntity>(listDirective: ConcernListDirective<T>): IComponentColumn<T> {
    return {
      label: 'Actions',
      type: 'component',
      className: 'list-control',
      headerClassName: 'list-control',
      component: ActionsButtonComponent,
      instanceTaken: (componentRef: ComponentRef<ActionsButtonComponent<T>>) => {
        componentRef.instance.onMouseenter
          .pipe(listDirective.takeUntil())
          .subscribe((row: T) => {
            listDirective.rewriteRow(row);
          });
      },
    };
  }

  static updateColumn(): IComponentColumn<any> {
    return {
      label: 'Upgrade',
      type: 'component',
      className: 'list-control',
      headerClassName: 'list-control',
      component: UpgradeComponent,
    };
  }

  static importColumn<T>(listDirective: AdwpListDirective<T>): IButtonsColumn<T> {
    return {
      label: 'Import',
      type: 'buttons',
      className: 'list-control',
      headerClassName: 'list-control',
      buttons: [{
        icon: 'import_export',
        callback: (row) => listDirective.baseListDirective.listEvents({ cmd: 'import', row }),
      }]
    };
  }

  static configColumn<T>(listDirective: AdwpListDirective<T>): IButtonsColumn<T> {
    return {
      label: 'Config',
      type: 'buttons',
      className: 'list-control',
      headerClassName: 'list-control',
      buttons: [{
        icon: 'settings',
        callback: (row) => listDirective.baseListDirective.listEvents({ cmd: 'config', row }),
      }]
    };
  }

  static bundleColumn(): IValueColumn<any> {
    return {
      label: 'Bundle',
      sort: 'prototype_display_name',
      value: (row) => [row.prototype_display_name || row.prototype_name, row.prototype_version, row.edition].join(' '),
    };
  }

  static deleteColumn<T>(listDirective: AdwpListDirective<T>): IButtonsColumn<T> {
    return {
      type: 'buttons',
      className: 'list-control',
      headerClassName: 'list-control',
      buttons: [{
        icon: 'delete',
        callback: (row, event) => listDirective.delete(event, row),
      }]
    };
  }

  static providerColumn(): ILinkColumn<any> {
    return {
      type: 'link',
      label: 'Provider',
      sort: 'provider_name',
      value: row => row.provider_name,
      url: row => `/provider/${row.provider_id}`,
    };
  }

  static keyColumn(): IValueColumn<any> {
    return {
      label: 'Parameter',
      value: (row) => row.key,
    };
  }

  static valueColumn(): IValueColumn<any> {
    return {
      label: 'Value',
      className: 'width30pr',
      headerClassName: 'width30pr',
      value: (row) => row.value,
    };
  }

  static maintenanceModeColumn<T>(listDirective: AdwpListDirective<T>): IComponentColumn<T> {
    return {
      type: 'component',
      className: 'list-control',
      headerClassName: 'list-control',
      component: MaintenanceModeButtonComponent,
      instanceTaken: (componentRef: ComponentRef<MaintenanceModeButtonComponent<T>>) => {
        componentRef.instance.onClick
        .pipe(listDirective.takeUntil())
        .subscribe(({event, value}) => listDirective.maintenanceModeToggle(event, value));
      }
    };
  }

}
