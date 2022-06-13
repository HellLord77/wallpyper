from . import _utils


class Windows:
    class Data:
        class Xml:
            class Dom:
                XmlDocument = _utils.XmlDocument

    class Foundation:
        AsyncActionCompletedHandler = _utils.AsyncActionCompletedHandler
        AsyncAction = _utils.AsyncAction
        PropertyValue = _utils.PropertyValue
        Uri = _utils.Uri
        WwwFormUrlDecoder = _utils.WwwFormUrlDecoder

        AsyncOperationProgressHandlerUINT64UINT64 = _utils.AsyncOperationProgressHandlerUINT64UINT64

        AsyncOperationWithProgressUINT64UINT64 = _utils.AsyncOperationWithProgressUINT64UINT64

        AsyncOperationWithProgressCompletedHandlerUINT64UINT64 = _utils.AsyncOperationWithProgressCompletedHandlerUINT64UINT64

        AsyncOperationCompletedHandlerRandomAccessStream = _utils.AsyncOperationCompletedHandlerRandomAccessStream

        AsyncOperationRandomAccessStream = _utils.AsyncOperationRandomAccessStream

        TypedEventHandlerToastNotificationInspectable = _utils.TypedEventHandlerToastNotificationInspectable
        TypedEventHandlerToastNotificationToastDismissedEventArgs = _utils.TypedEventHandlerToastNotificationToastDismissedEventArgs
        TypedEventHandlerToastNotificationToastFailedEventArgs = _utils.TypedEventHandlerToastNotificationToastFailedEventArgs

        class Collections:
            IterableSetterBase = _utils.IterableSetterBase

            IteratorSetterBase = _utils.IteratorSetterBase

            VectorGradientStop = _utils.VectorGradientStop
            VectorMenuFlyoutItemBase = _utils.VectorMenuFlyoutItemBase
            VectorSetterBase = _utils.VectorSetterBase
            VectorUIElement = _utils.VectorUIElement

            KeyValuePairHSTRINGHSTRING = _utils.KeyValuePairHSTRINGHSTRING

            MapHSTRINGHSTRING = _utils.MapHSTRINGHSTRING

    class Storage:
        class Streams:
            FileInputStream = _utils.FileInputStream
            FileOutputStream = _utils.FileOutputStream
            FileRandomAccessStream = _utils.FileRandomAccessStream
            RandomAccessStream = _utils.RandomAccessStream

    class System:
        class UserProfile:
            LockScreen = _utils.LockScreen
            UserInformation = _utils.UserInformation

    class UI:
        Colors = _utils.Colors

        class Composition:
            SpringVector3NaturalMotionAnimation = _utils.SpringVector3NaturalMotionAnimation
            Vector3NaturalMotionAnimation = _utils.Vector3NaturalMotionAnimation
            NaturalMotionAnimation = _utils.NaturalMotionAnimation
            CompositionAnimation = _utils.CompositionAnimation
            CompositionObject = _utils.CompositionObject
            Compositor = _utils.Compositor

        class Core:
            CoreDispatcher = _utils.CoreDispatcher
            DispatchedHandler = _utils.DispatchedHandler

        class Notifications:
            ToastActivatedEventArgs = _utils.ToastActivatedEventArgs
            ToastDismissedEventArgs = _utils.ToastDismissedEventArgs
            ToastFailedEventArgs = _utils.ToastFailedEventArgs
            ToastNotification = _utils.ToastNotification
            ToastNotificationManager = _utils.ToastNotificationManager
            ToastNotifier = _utils.ToastNotifier

        class Xaml:
            RoutedEventHandler = _utils.RoutedEventHandler

            ApplicationInitializationCallback = _utils.ApplicationInitializationCallback
            ApplicationInitializationCallbackParams = _utils.ApplicationInitializationCallbackParams
            Application = _utils.Application
            DependencyObject = _utils.DependencyObject
            DependencyProperty = _utils.DependencyProperty
            FrameworkElement = _utils.FrameworkElement
            PropertyMetadata = _utils.PropertyMetadata
            RoutedEventArgs = _utils.RoutedEventArgs
            Setter = _utils.Setter
            ScalarTransition = _utils.ScalarTransition
            SetterBase = _utils.SetterBase
            SetterBaseCollection = _utils.SetterBaseCollection
            Style = _utils.Style
            UIElement = _utils.UIElement
            Window = _utils.Window

            class Controls:
                AppBarButton = _utils.AppBarButton
                Button = _utils.Button
                ContentControl = _utils.ContentControl
                Control = _utils.Control
                DropDownButton = _utils.DropDownButton
                HyperlinkButton = _utils.HyperlinkButton
                IconElement = _utils.IconElement
                ItemsControl = _utils.ItemsControl
                MenuFlyout = _utils.MenuFlyout
                MenuFlyoutItem = _utils.MenuFlyoutItem
                MenuFlyoutItemBase = _utils.MenuFlyoutItemBase
                MenuFlyoutPresenter = _utils.MenuFlyoutPresenter
                Panel = _utils.Panel
                StackPanel = _utils.StackPanel
                SymbolIcon = _utils.SymbolIcon
                TextBlock = _utils.TextBlock
                ToolTip = _utils.ToolTip
                ToolTipService = _utils.ToolTipService
                UIElementCollection = _utils.UIElementCollection

                class Primitives:
                    ButtonBase = _utils.ButtonBase
                    FlyoutBase = _utils.FlyoutBase
                    FlyoutShowOptions = _utils.FlyoutShowOptions
                    RepeatButton = _utils.RepeatButton
                    ToggleButton = _utils.ToggleButton

            class Hosting:
                DesktopWindowXamlSource = _utils.DesktopWindowXamlSource
                WindowsXamlManager = _utils.WindowsXamlManager

            class Input:
                PointerEventHandler = _utils.PointerEventHandler

            class Markup:
                XamlReader = _utils.XamlReader

            class Media:
                Brush = _utils.Brush
                GradientStop = _utils.GradientStop
                GradientBrush = _utils.GradientBrush
                LinearGradientBrush = _utils.LinearGradientBrush
                SolidColorBrush = _utils.SolidColorBrush
                VisualTreeHelper = _utils.VisualTreeHelper
