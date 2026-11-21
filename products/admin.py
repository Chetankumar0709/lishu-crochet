from django.contrib import admin

from .models import Category, ContactMessage, Product, ProductImage, SiteSettings, Testimonial


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name", "description")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "is_featured", "updated_at")
    list_filter = ("category", "is_featured")
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ProductImageInline]


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Identity", {"fields": ("business_name", "logo", "hero_text", "copyright_text")}),
        ("Contact", {"fields": ("phone_number", "whatsapp_number", "email", "address")}),
        ("Social", {"fields": ("instagram_link", "facebook_link", "youtube_link")}),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "rating", "is_active")
    list_filter = ("is_active", "rating")
    search_fields = ("customer_name", "review")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "created_at")
    readonly_fields = ("name", "email", "phone", "message", "created_at")
    search_fields = ("name", "email", "message")

    def has_add_permission(self, request):
        return False
