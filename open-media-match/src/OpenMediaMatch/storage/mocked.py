# Copyright (c) Meta Platforms, Inc. and affiliates.

import typing as t

from threatexchange.content_type.photo import PhotoContent
from threatexchange.content_type.video import VideoContent
from threatexchange.exchanges.signal_exchange_api import TSignalExchangeAPICls
from threatexchange.exchanges.impl.static_sample import StaticSampleSignalExchangeAPI
from threatexchange.signal_type.pdq.signal import PdqSignal
from threatexchange.signal_type.md5 import VideoMD5Signal

from OpenMediaMatch.storage import interface
from OpenMediaMatch.storage.interface import SignalTypeConfig


class MockedUnifiedStore(interface.IUnifiedStore):
    """
    Provides plausible default values for all store interfaces.
    """

    def get_content_type_configs(self) -> t.Mapping[str, interface.ContentTypeConfig]:
        return {
            c.get_name(): interface.ContentTypeConfig(True, c)
            for c in (PhotoContent, VideoContent)
        }

    def get_exchange_type_configs(self) -> t.Mapping[str, TSignalExchangeAPICls]:
        return {e.get_name(): e for e in (StaticSampleSignalExchangeAPI,)}

    def get_signal_type_configs(self) -> t.Mapping[str, SignalTypeConfig]:
        return {
            s.get_name(): interface.SignalTypeConfig(True, s)
            for s in (PdqSignal, VideoMD5Signal)
        }
