Summary: ClanLib, the platform independent game SDK [development package]
Name: ClanLib-devel
Version: 0.1.13
Release: 2
Copyright: LGPL
Group: Libraries
Source: clanlib-devel-0.1.13.tgz
URL: http://clanlib.org
%description
The ClanLib SDK is designed to provide a platform independent game SDK using
a cleaner and more object oriented interface, than the traditional way it is
done in DirectX, SDL and such. The goals is to avoid game developers
having to constantly reinvent the wheel, by providing smarter ways to eg.
load surfaces.
This is the development add-on package that includes the header files needed
to compile new ClanLib applications.

%prep
%setup
%build
./configure -prefix=/usr
make
%install
make install
%files
/usr/bin/datafile_compiler
/usr/include/ClanLib/clanlib.h
/usr/include/ClanLib/clanlayer2.h
/usr/include/ClanLib/Common/array.h
/usr/include/ClanLib/Common/chunk_allocator.h
/usr/include/ClanLib/Common/clanstring.h
/usr/include/ClanLib/Common/error.h
/usr/include/ClanLib/Common/formatted_data.h
/usr/include/ClanLib/Common/hashtable.h
/usr/include/ClanLib/Common/link.h
/usr/include/ClanLib/Common/matrix.h
/usr/include/ClanLib/Common/memory.h
/usr/include/ClanLib/Common/queue.h
/usr/include/ClanLib/Common/singlelink.h
/usr/include/ClanLib/Common/stack.h
/usr/include/ClanLib/Common/vector.h
/usr/include/ClanLib/Layer1/Display/API/cliprect.h
/usr/include/ClanLib/Layer1/Display/API/display.h
/usr/include/ClanLib/Layer1/Display/API/displaycard.h
/usr/include/ClanLib/Layer1/Display/API/palette.h
/usr/include/ClanLib/Layer1/Display/API/pixelformat.h
/usr/include/ClanLib/Layer1/Display/API/surface.h
/usr/include/ClanLib/Layer1/Display/API/surfacepriority.h
/usr/include/ClanLib/Layer1/Display/API/surfaceprovider.h
/usr/include/ClanLib/Layer1/Display/API/vidmode.h
/usr/include/ClanLib/Layer1/Sound/API/sound.h
/usr/include/ClanLib/Layer1/Sound/API/soundbuffer.h
/usr/include/ClanLib/Layer1/Sound/API/soundbuffer_session.h
/usr/include/ClanLib/Layer1/Sound/API/soundformat.h
/usr/include/ClanLib/Layer1/Sound/API/static_soundprovider.h
/usr/include/ClanLib/Layer1/Sound/API/stream_soundprovider.h
/usr/include/ClanLib/Layer1/Input/API/input.h
/usr/include/ClanLib/Layer1/Input/API/inputaxis.h
/usr/include/ClanLib/Layer1/Input/API/inputbuffer.h
/usr/include/ClanLib/Layer1/Input/API/inputbutton.h
/usr/include/ClanLib/Layer1/Input/API/inputcursor.h
/usr/include/ClanLib/Layer1/Input/API/inputdevice.h
/usr/include/ClanLib/Layer1/Input/API/inputhat.h
/usr/include/ClanLib/Layer1/Input/API/keyboard.h
/usr/include/ClanLib/Layer1/IOData/API/endian.h
/usr/include/ClanLib/Layer1/IOData/API/inputsource.h
/usr/include/ClanLib/Layer1/IOData/API/inputsource_provider.h
/usr/include/ClanLib/Layer1/IOData/API/outputsource.h
/usr/include/ClanLib/Layer1/IOData/API/outputsource_provider.h
/usr/include/ClanLib/Layer1/Network/API/netcomputer.h
/usr/include/ClanLib/Layer1/Network/API/netgame.h
/usr/include/ClanLib/Layer1/Network/API/netgroup.h
/usr/include/ClanLib/Layer1/Network/API/netmessage.h
/usr/include/ClanLib/Layer1/Network/API/netport.h
/usr/include/ClanLib/Layer1/Network/API/network.h
/usr/include/ClanLib/Layer1/System/API/cl_assert.h
/usr/include/ClanLib/Layer1/System/API/clanapp.h
/usr/include/ClanLib/Layer1/System/API/system.h
/usr/include/ClanLib/Layer1/System/API/timer_manager.h
/usr/include/ClanLib/Layer2/InputConverters/inputaxis_basic.h
/usr/include/ClanLib/Layer2/InputConverters/inputaxis_group.h
/usr/include/ClanLib/Layer2/InputConverters/inputbutton_basic.h
/usr/include/ClanLib/Layer2/InputConverters/inputbutton_group.h
/usr/include/ClanLib/Layer2/InputConverters/inputbutton_to_axis_analog.h
/usr/include/ClanLib/Layer2/InputConverters/inputbutton_to_axis_digital.h
/usr/include/ClanLib/Layer2/Misc/font.h
/usr/include/ClanLib/Layer2/Misc/layermanager.h
/usr/include/ClanLib/Layer2/NetPorts/netport_filetransfer.h
/usr/include/ClanLib/Layer2/NetPorts/netport_portnumbers.h
/usr/include/ClanLib/Layer2/NetPorts/netport_sms.h
/usr/include/ClanLib/Layer2/Resources/resource_manager.h
/usr/include/ClanLib/Layer2/Resources/resourcetype_font.h
/usr/include/ClanLib/Layer2/Resources/resourcetype_palette.h
/usr/include/ClanLib/Layer2/Resources/resourcetype_raw.h
/usr/include/ClanLib/Layer2/Resources/resourcetype_sample.h
/usr/include/ClanLib/Layer2/Resources/resourcetype_surface.h
/usr/include/ClanLib/Layer2/StaticSoundProviders/raw_sample.h
/usr/include/ClanLib/Layer2/StaticSoundProviders/wave_sample.h
/usr/include/ClanLib/Layer2/StreamSoundProviders/streamed_raw_sample.h
/usr/include/ClanLib/Layer2/StreamSoundProviders/streamed_wave_sample.h
/usr/include/ClanLib/Layer2/SurfaceProviders/generic_surfaceprovider.h
/usr/include/ClanLib/Layer2/SurfaceProviders/provider_convpoly.h
/usr/include/ClanLib/Layer2/SurfaceProviders/provider_convpoly_basics.h
/usr/include/ClanLib/Layer2/SurfaceProviders/provider_empty.h
/usr/include/ClanLib/Layer2/SurfaceProviders/provider_fli.h
/usr/include/ClanLib/Layer2/SurfaceProviders/provider_pcx.h
/usr/include/ClanLib/Layer2/SurfaceProviders/provider_png.h
/usr/include/ClanLib/Layer2/SurfaceProviders/provider_targa.h
/usr/include/ClanLib/Layer2/SurfaceProviders/sprite.h
/usr/include/ClanLib/Layer2/SurfaceProviders/sprite_subarray_provider.h
/usr/include/ClanLib/Layer2/SurfaceProviders/sprite_subsection_provider.h
/usr/include/ClanLib/Layer2/SurfaceProviders/surface_manager.h
