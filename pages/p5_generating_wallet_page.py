class GeneratingWalletPage:
    _button_generating = ['xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button']
    _subtitle_owner_of = ['id', 'io.zerion.android:id/ownerOf']
    _ok_lets_go_button = ['id', 'io.zerion.android:id/button']
    _created_wallet_number = ['xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/androidx.cardview.widget.CardView/android.view.ViewGroup/android.view.ViewGroup/android.view.View']

    @classmethod
    def get_button_generating(cls):
        return cls._button_generating

    @classmethod
    def get_subtitle_owner_of(cls):
        return cls._subtitle_owner_of

    @classmethod
    def get_ok_lets_go_button(cls):
        return cls._ok_lets_go_button

    @classmethod
    def get_created_wallet_number(cls):
        return cls._created_wallet_number


