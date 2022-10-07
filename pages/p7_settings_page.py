class SettingsPage:

    _manage_wallets_button = ['xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[5]']
    _zerion_wallets = ['xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout']
    _first_wallet = ['xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup']
    _private_key = ['xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.TextView']
    _show_button = ['id', 'io.zerion.android:id/actionButton']
    _display_private_key_button = ['id', 'io.zerion.android:id/buttonDisplay']
    _QR_code = ['id', 'io.zerion.android:id/qrCode']
    _copy_to_clipboard = ['id', 'io.zerion.android:id/buttonCopy']
    _import_wallet_button = ['id', 'io.zerion.android:id/button']
    _enter_seed_phrase_or_private_key = ['id', 'io.zerion.android:id/editTextView']
    _import_button = ['id', 'io.zerion.android:id/importButton']
    _wallets_ready_to_import = ['id', 'io.zerion.android:id/title']
    _wallet_for_import = ['xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView[1]']
    _continue_button = ['id', 'io.zerion.android:id/actionButton']
    _all_done = ['xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/androidx.cardview.widget.CardView/android.widget.TextView']
    _finish_button = ['id', 'io.zerion.android:id/button']




    @classmethod
    def get_manage_wallets_button(cls):
        return cls._manage_wallets_button

    @classmethod
    def get_zerion_wallets(cls):
        return cls._zerion_wallets

    @classmethod
    def get_first_wallet(cls):
        return cls._first_wallet

    @classmethod
    def get_private_key(cls):
        return cls._private_key

    @classmethod
    def get_show_button(cls):
        return cls._show_button

    @classmethod
    def get_display_private_key_button(cls):
        return cls._display_private_key_button

    @classmethod
    def get_QR_code(cls):
        return cls._QR_code

    @classmethod
    def get_copy_to_clipboard(cls):
        return cls._copy_to_clipboard

    @classmethod
    def get_import_wallet_button(cls):
        return cls._import_wallet_button

    @classmethod
    def get_enter_seed_phrase_or_private_key(cls):
        return cls._enter_seed_phrase_or_private_key

    @classmethod
    def get_import_button(cls):
        return cls._import_button

    @classmethod
    def get_wallets_ready_to_import(cls):
        return cls._wallets_ready_to_import

    @classmethod
    def get_wallet_for_import(cls):
        return cls._wallet_for_import

    @classmethod
    def get_continue_button(cls):
        return cls._continue_button

    @classmethod
    def get_all_done(cls):
        return cls._all_done

    @classmethod
    def get_finish_button(cls):
        return cls._finish_button





