from typing import ClassVar, Any

from .base_multikey import partial_create_verb_params
from .gamepad import Gamepad_Actionset
from ..actionset import Actionset
from ..._shared.constants import INPUT_TYPE
from ..._shared.types import VerbParamDict, Partial_VerbParamDict


class HSR_GP_Actionset(Gamepad_Actionset):
    '''
    Gamepad-based Actionset that implements the controls for the game
    `Honkai Star Rail`
    '''
    # Class variables:
    name: ClassVar[str] = 'Honkai Star Rail (Gamepad)'
    # ----------------------------------------------------------------------------

    '''
    HSR Controls (XInput):
    
    Action      | Default Layout |
    ------------|----------------|
    Swap Basic  | {X}            |
    Skill       | {Y}            |
    Cast Ability| {A}            |
    Target Right| {RT}           |
    Target Left | {LT}           |
    B Button    | {B}            |
    '''

    key_dict: ClassVar[dict[str, str]] = {
        'basic': 'x',
        'skill': 'y',
        'cast': 'a',
        'target_left': 'lt',
        'target_right': 'rt',
        'b_button': 'b',
    }

    # ----------------------------------------------------------------------------

    def __init__(
            self,
            doc_url: str = "",
            **kwargs: Any
    ) -> None:
        '''
        Gamepad-based Actionset that implements the controls for the game
        `Honkai Star Rail`
        '''
        super().__init__(doc_url=doc_url, **kwargs)
        self.verb_dict = _build_verb_dict(self.action_prefix)


def _build_verb_dict(action_prefix: str) -> dict[str, list[VerbParamDict]]:
    '''
    Build the dictionary of verbs for this actionset.
    '''
    verb_param: Partial_VerbParamDict = partial_create_verb_params(
        duration=50,
        delay=0,
        min_time=1,
        max_time=100,
        input_type=INPUT_TYPE.PRESS_KEY
    )

    verb_dict = dict[str, list[VerbParamDict]] = {
        'cast': [verb_param(key='cast', duration=50)],
        'basic': [verb_param(key='basic', duration=50)],
        'skill': [verb_param(key='skill', duration=50)],
        'target_right': [verb_param(key='target_right', duration=50)],
        'b': [verb_param(key='b_button', duration=50)],
    }

    key: str

    for key in list(verb_dict.keys()):
        prefixed_key: str = f'{action_prefix}{key}'
        verb_dict[prefixed_key] = verb_dict[key]

    return verb_dict


_EXPORT_CLASSES_: list[type[Actionset]] = [
    HSR_GP_Actionset,
]
