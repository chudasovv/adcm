import { Directive } from '@angular/core';
import { BaseDirective } from '@adwp-ui/widgets';

import { PopoverInput } from '../directives/popover.directive';

export type PopoverEventFunc = (event: any) => void;

@Directive({
  selector: '[appAbstractPopoverContent]',
})
export abstract class PopoverContentDirective extends BaseDirective {

  abstract data: PopoverInput;

  event?: PopoverEventFunc;

}
