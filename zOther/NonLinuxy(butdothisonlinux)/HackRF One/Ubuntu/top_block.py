#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Tue Dec 13 11:19:29 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2e6
        self.channel_width = channel_width = 200.0e3
        self.init_decimation_int = init_decimation_int = int(samp_rate/channel_width)
        self.RR_interp = RR_interp = 12.0
        self.RR_dec = RR_dec = 5.0
        self.quad_rate = quad_rate = samp_rate/init_decimation_int*(RR_interp/RR_dec)
        self.channel_freq_SWtune = channel_freq_SWtune = 451e6
        self.center_freq_HWtune = center_freq_HWtune = 450e6

        ##################################################
        # Blocks
        ##################################################
        _channel_freq_SWtune_sizer = wx.BoxSizer(wx.VERTICAL)
        self._channel_freq_SWtune_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_channel_freq_SWtune_sizer,
        	value=self.channel_freq_SWtune,
        	callback=self.set_channel_freq_SWtune,
        	label='channel_freq_SWtune',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._channel_freq_SWtune_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_channel_freq_SWtune_sizer,
        	value=self.channel_freq_SWtune,
        	callback=self.set_channel_freq_SWtune,
        	minimum=400e6,
        	maximum=500e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_channel_freq_SWtune_sizer)
        _center_freq_HWtune_sizer = wx.BoxSizer(wx.VERTICAL)
        self._center_freq_HWtune_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_center_freq_HWtune_sizer,
        	value=self.center_freq_HWtune,
        	callback=self.set_center_freq_HWtune,
        	label='center_freq_HWtune',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._center_freq_HWtune_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_center_freq_HWtune_sizer,
        	value=self.center_freq_HWtune,
        	callback=self.set_center_freq_HWtune,
        	minimum=400e6,
        	maximum=500e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_center_freq_HWtune_sizer)
        self.wxgui_fftsink2_0_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=channel_freq_SWtune,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=True,
        	avg_alpha=None,
        	title='FFT Plot (multiplied)',
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=center_freq_HWtune,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=True,
        	avg_alpha=None,
        	title='FFT Plot',
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=int(RR_interp),
                decimation=int(RR_dec),
                taps=None,
                fractional_bw=None,
        )
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(center_freq_HWtune, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(0, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        self.low_pass_filter_0 = filter.fir_filter_ccf(init_decimation_int, firdes.low_pass(
        	1, samp_rate, 75e3, 25e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=quad_rate,
        	audio_decimation=10,
        )
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, center_freq_HWtune-channel_freq_SWtune, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.analog_wfm_rcv_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.wxgui_fftsink2_0_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.wxgui_fftsink2_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_wfm_rcv_0, 0))    

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_quad_rate(self.samp_rate/self.init_decimation_int*(self.RR_interp/self.RR_dec))
        self.set_init_decimation_int(int(self.samp_rate/self.channel_width))
        self.wxgui_fftsink2_0_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 75e3, 25e3, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_channel_width(self):
        return self.channel_width

    def set_channel_width(self, channel_width):
        self.channel_width = channel_width
        self.set_init_decimation_int(int(self.samp_rate/self.channel_width))

    def get_init_decimation_int(self):
        return self.init_decimation_int

    def set_init_decimation_int(self, init_decimation_int):
        self.init_decimation_int = init_decimation_int
        self.set_quad_rate(self.samp_rate/self.init_decimation_int*(self.RR_interp/self.RR_dec))

    def get_RR_interp(self):
        return self.RR_interp

    def set_RR_interp(self, RR_interp):
        self.RR_interp = RR_interp
        self.set_quad_rate(self.samp_rate/self.init_decimation_int*(self.RR_interp/self.RR_dec))

    def get_RR_dec(self):
        return self.RR_dec

    def set_RR_dec(self, RR_dec):
        self.RR_dec = RR_dec
        self.set_quad_rate(self.samp_rate/self.init_decimation_int*(self.RR_interp/self.RR_dec))

    def get_quad_rate(self):
        return self.quad_rate

    def set_quad_rate(self, quad_rate):
        self.quad_rate = quad_rate

    def get_channel_freq_SWtune(self):
        return self.channel_freq_SWtune

    def set_channel_freq_SWtune(self, channel_freq_SWtune):
        self.channel_freq_SWtune = channel_freq_SWtune
        self._channel_freq_SWtune_slider.set_value(self.channel_freq_SWtune)
        self._channel_freq_SWtune_text_box.set_value(self.channel_freq_SWtune)
        self.wxgui_fftsink2_0_0.set_baseband_freq(self.channel_freq_SWtune)
        self.analog_sig_source_x_0.set_frequency(self.center_freq_HWtune-self.channel_freq_SWtune)

    def get_center_freq_HWtune(self):
        return self.center_freq_HWtune

    def set_center_freq_HWtune(self, center_freq_HWtune):
        self.center_freq_HWtune = center_freq_HWtune
        self._center_freq_HWtune_slider.set_value(self.center_freq_HWtune)
        self._center_freq_HWtune_text_box.set_value(self.center_freq_HWtune)
        self.wxgui_fftsink2_0.set_baseband_freq(self.center_freq_HWtune)
        self.osmosdr_source_0.set_center_freq(self.center_freq_HWtune, 0)
        self.analog_sig_source_x_0.set_frequency(self.center_freq_HWtune-self.channel_freq_SWtune)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
