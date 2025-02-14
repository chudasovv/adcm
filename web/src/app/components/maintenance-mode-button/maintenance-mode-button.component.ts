import { Component, EventEmitter, Input, Output } from '@angular/core';
import { AdwpCellComponent } from "@adwp-ui/widgets";

export enum StatusType {
  On = 'on',
  Off = 'off',
  Disabled = 'disabled'
}

export interface Status {
  isButtonActive: boolean;
  isModeActive: boolean;
  color: string;
  tooltip: string;
}

@Component({
  selector: 'app-maintenance-mode-button',
  templateUrl: './maintenance-mode-button.component.html',
  styleUrls: ['./maintenance-mode-button.component.scss']
})
export class MaintenanceModeButtonComponent<T> implements AdwpCellComponent<T> {
  statuses: { [key in StatusType]: Status; } = {
    [StatusType.On]: {
      isButtonActive: true,
      isModeActive: true,
      color: 'on',
      tooltip: 'Turn maintenance mode OFF'
    },
    [StatusType.Off]: {
      isButtonActive: false,
      isModeActive: true,
      color: 'primary',
      tooltip:'Turn maintenance mode ON'
    },
    [StatusType.Disabled]: {
      isButtonActive: false,
      isModeActive: false,
      color: 'primary',
      tooltip: 'Maintenance mode is not available'
    }
  }

  get maintenanceModeStatus(): string {
   return this?.row?.maintenance_mode;
  }

  get status(): Status {
    return this.statuses[this.maintenanceModeStatus];
  }

  @Input() row: any;
  @Output() onClick = new EventEmitter();

  ngOnInit(): void {}

  clickCell(event: MouseEvent, row: T): void {
    if (this.maintenanceModeStatus !== StatusType.Disabled && this.maintenanceModeStatus === StatusType.On) {
      this.row.maintenance_mode = StatusType.Off;
    } else if (this.maintenanceModeStatus !== StatusType.Disabled && this.maintenanceModeStatus === StatusType.Off) {
      this.row.maintenance_mode = StatusType.On;
    }

    this.onClick.emit({ event, value: { id: this.row['id'], maintenance_mode: this.row.maintenance_mode } });
  }

  preventIfDisabled(event) {
    if (!this.status?.isModeActive) {
      event.stopPropagation();
      event.preventDefault();
    }
  }
}
