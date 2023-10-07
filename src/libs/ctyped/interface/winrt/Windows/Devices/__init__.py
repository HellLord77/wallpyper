from __future__ import annotations as _

from typing import Callable as _Callable

from .Adc import Provider as _Windows_Devices_Adc_Provider
from .Gpio import Provider as _Windows_Devices_Gpio_Provider
from .I2c import Provider as _Windows_Devices_I2c_Provider
from .Pwm import Provider as _Windows_Devices_Pwm_Provider
from .Spi import Provider as _Windows_Devices_Spi_Provider
from ... import inspectable as _inspectable
from ..... import type as _type
from ....._utils import _Pointer


class ILowLevelDevicesAggregateProvider(_inspectable.IInspectable):
    get_AdcControllerProvider: _Callable[[_Pointer[_Windows_Devices_Adc_Provider.IAdcControllerProvider]],  # value
                                         _type.HRESULT]
    get_PwmControllerProvider: _Callable[[_Pointer[_Windows_Devices_Pwm_Provider.IPwmControllerProvider]],  # value
                                         _type.HRESULT]
    get_GpioControllerProvider: _Callable[[_Pointer[_Windows_Devices_Gpio_Provider.IGpioControllerProvider]],  # value
                                          _type.HRESULT]
    get_I2cControllerProvider: _Callable[[_Pointer[_Windows_Devices_I2c_Provider.II2cControllerProvider]],  # value
                                         _type.HRESULT]
    get_SpiControllerProvider: _Callable[[_Pointer[_Windows_Devices_Spi_Provider.ISpiControllerProvider]],  # value
                                         _type.HRESULT]


class ILowLevelDevicesAggregateProviderFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Windows_Devices_Adc_Provider.IAdcControllerProvider,  # adc
                       _Windows_Devices_Pwm_Provider.IPwmControllerProvider,  # pwm
                       _Windows_Devices_Gpio_Provider.IGpioControllerProvider,  # gpio
                       _Windows_Devices_I2c_Provider.II2cControllerProvider,  # i2c
                       _Windows_Devices_Spi_Provider.ISpiControllerProvider,  # spi
                       _Pointer[ILowLevelDevicesAggregateProvider]],  # value
                      _type.HRESULT]


class ILowLevelDevicesController(_inspectable.IInspectable):
    pass


class ILowLevelDevicesControllerStatics(_inspectable.IInspectable, factory=True):
    get_DefaultProvider: _Callable[[_Pointer[ILowLevelDevicesAggregateProvider]],  # value
                                   _type.HRESULT]
    put_DefaultProvider: _Callable[[ILowLevelDevicesAggregateProvider],  # value
                                   _type.HRESULT]
