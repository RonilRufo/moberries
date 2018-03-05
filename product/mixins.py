# -*- coding: utf-8 -*-


class UpdateSerializerMixin(object):
    """
    This mixin will allow partial update on PUT requests
    """

    def __init__(self, *args, **kwargs):

        super(UpdateSerializerMixin, self).__init__(*args, **kwargs)

        if self.instance and hasattr(self, 'initial_data') and self.initial_data:
            self.partial = True
