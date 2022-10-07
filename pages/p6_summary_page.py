class SummaryPage:
    _button_backup_1min = ['id', 'io.zerion.android:id/actionButton']
    _button_i_will_take_risk = ['id', 'io.zerion.android:id/skipButton']
    _popup_button_update_later = ['id', 'android:id/button2']
    _button_got_it = ['id', 'io.zerion.android:id/button']
    _button_show_seed_phrase = ['xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button']
    _button_confirm_phrase = ['id', 'io.zerion.android:id/button']
    _number = ['id', 'io.zerion.android:id/number']
    _nicely_done = ['id', 'io.zerion.android:id/successTitleTV']
    _finish_button = ['id', 'io.zerion.android:id/finishButton']
    _warning_notification = ['xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.TextView[1]']
    _settings_button = ['id', 'io.zerion.android:id/tabs_settings']
    _summery = ['id', 'io.zerion.android:id/tabs_wallet']
    _first_created_wallet = ['xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/androidx.cardview.widget.CardView/android.view.ViewGroup/android.widget.TextView[1]']
    _imported_wallet = ['xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]/androidx.cardview.widget.CardView/android.view.ViewGroup/android.widget.TextView[1]']
    _add_wallet = ['id', 'io.zerion.android:id/navigation_add']


    @classmethod
    def get_button_backup_1min(cls):
        return cls._button_backup_1min

    @classmethod
    def get_popup_button_update_later(cls):
        return cls._popup_button_update_later

    @classmethod
    def get_button_got_it(cls):
        return cls._button_got_it

    @classmethod
    def get_button_show_seed_phrase(cls):
        return cls._button_show_seed_phrase

    @classmethod
    def get_button_confirm_phrase(cls):
        return cls._button_confirm_phrase

    @classmethod
    def get_number(cls):
        return cls._number

    @classmethod
    def get_nicely_done(cls):
        return cls._nicely_done

    @classmethod
    def get_finish_button(cls):
        return cls._finish_button

    @classmethod
    def get_warning_notification(cls):
        return cls._warning_notification

    @classmethod
    def get_settings_button(cls):
        return cls._settings_button

    @classmethod
    def get_summery(cls):
        return cls._summery

    @classmethod
    def get_imported_wallet(cls):
        return cls._imported_wallet

    @classmethod
    def get_button_i_will_take_risk(cls):
        return cls._button_i_will_take_risk

    @classmethod
    def get_add_wallet(cls):
        return cls._add_wallet

    @classmethod
    def get_first_created_wallet(cls):
        return cls._first_created_wallet



